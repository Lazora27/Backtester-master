import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und DemandIndex
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'DemandIndex': 1.0
        })
    )
