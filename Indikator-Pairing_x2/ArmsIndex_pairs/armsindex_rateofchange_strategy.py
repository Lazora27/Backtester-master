import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und RateOfChange
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'RateOfChange': 1.0
        })
    )
