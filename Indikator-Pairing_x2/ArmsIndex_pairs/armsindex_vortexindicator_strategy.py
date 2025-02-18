import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'VortexIndicator': 1.0
        })
    )
