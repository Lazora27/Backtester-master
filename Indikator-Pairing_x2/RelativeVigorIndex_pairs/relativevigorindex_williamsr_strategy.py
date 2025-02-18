import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeVigorIndex_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeVigorIndex und WilliamsR
    """
    
    params = (
        ('indicators', {
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'RelativeVigorIndex': 1.0,
            'WilliamsR': 1.0
        })
    )
