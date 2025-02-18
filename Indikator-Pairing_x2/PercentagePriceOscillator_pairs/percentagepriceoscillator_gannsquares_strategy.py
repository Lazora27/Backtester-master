import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und GannSquares
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'GannSquares': 1.0
        })
    )
