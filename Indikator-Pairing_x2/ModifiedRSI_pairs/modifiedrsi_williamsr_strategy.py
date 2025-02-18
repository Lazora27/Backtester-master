import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und WilliamsR
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'WilliamsR': 1.0
        })
    )
