import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HeikenAshiSmoothed_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HeikenAshiSmoothed und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'HeikenAshiSmoothed': {
                'class': HeikenAshiSmoothed,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiSmoothed'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'HeikenAshiSmoothed': 1.0,
            'AccelerationBands': 1.0
        })
    )
