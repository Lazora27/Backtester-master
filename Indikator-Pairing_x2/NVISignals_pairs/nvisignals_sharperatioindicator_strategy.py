import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
