import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MLForecast_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MLForecast und FisherSignals
    """
    
    params = (
        ('indicators', {
            'MLForecast': {
                'class': MLForecast,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MLForecast'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'MLForecast': 1.0,
            'FisherSignals': 1.0
        })
    )
