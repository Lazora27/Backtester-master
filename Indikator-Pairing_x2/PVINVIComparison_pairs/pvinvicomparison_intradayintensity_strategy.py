import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'IntradayIntensity': 1.0
        })
    )
