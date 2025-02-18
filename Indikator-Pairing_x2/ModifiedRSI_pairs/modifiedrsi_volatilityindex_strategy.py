import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'VolatilityIndex': 1.0
        })
    )
