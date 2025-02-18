import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DetrendedPriceOscillator_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DetrendedPriceOscillator und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'DetrendedPriceOscillator': {
                'class': DetrendedPriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DetrendedPriceOscillator1'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'DetrendedPriceOscillator': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
