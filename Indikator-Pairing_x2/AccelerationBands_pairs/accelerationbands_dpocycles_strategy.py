import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und DPOCycles
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'DPOCycles': 1.0
        })
    )
