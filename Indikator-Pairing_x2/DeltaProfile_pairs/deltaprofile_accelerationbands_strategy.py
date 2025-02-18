import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'AccelerationBands': 1.0
        })
    )
