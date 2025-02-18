import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketFacilitationMomentum_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketFacilitationMomentum und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'MarketFacilitationMomentum': {
                'class': MarketFacilitationMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationMomentum'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'MarketFacilitationMomentum': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
