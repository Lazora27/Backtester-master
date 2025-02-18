import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SineWaveAdaptive_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SineWaveAdaptive und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'SineWaveAdaptive': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
