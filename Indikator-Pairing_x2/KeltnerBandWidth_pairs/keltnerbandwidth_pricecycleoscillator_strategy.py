import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
