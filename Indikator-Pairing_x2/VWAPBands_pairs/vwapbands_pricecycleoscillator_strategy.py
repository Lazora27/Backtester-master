import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
