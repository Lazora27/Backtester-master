import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'AccelerationBands': 1.0
        })
    )
