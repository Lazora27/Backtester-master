import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
