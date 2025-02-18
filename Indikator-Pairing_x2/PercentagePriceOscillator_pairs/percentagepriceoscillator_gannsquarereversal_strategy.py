import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'GannSquareReversal': 1.0
        })
    )
