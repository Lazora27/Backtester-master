import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
