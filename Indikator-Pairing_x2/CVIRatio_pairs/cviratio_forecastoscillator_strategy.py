import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_ForecastOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und ForecastOscillator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'ForecastOscillator': 1.0
        })
    )
