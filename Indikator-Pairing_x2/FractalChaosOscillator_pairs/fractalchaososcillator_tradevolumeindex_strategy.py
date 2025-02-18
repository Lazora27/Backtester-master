import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
