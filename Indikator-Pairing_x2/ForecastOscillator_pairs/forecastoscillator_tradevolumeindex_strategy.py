import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
