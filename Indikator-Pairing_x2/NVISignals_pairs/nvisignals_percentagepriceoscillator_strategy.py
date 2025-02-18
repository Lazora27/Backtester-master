import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_PercentagePriceOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und PercentagePriceOscillator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'PercentagePriceOscillator': 1.0
        })
    )
