import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TradeVolumeIndex_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TradeVolumeIndex und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'TradeVolumeIndex': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
