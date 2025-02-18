import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'AccelerationBands': 1.0
        })
    )
