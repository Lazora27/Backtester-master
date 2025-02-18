import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
