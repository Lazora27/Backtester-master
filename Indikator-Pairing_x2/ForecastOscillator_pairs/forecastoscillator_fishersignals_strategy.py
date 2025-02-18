import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'FisherSignals': 1.0
        })
    )
