import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und VWAPBands
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'VWAPBands': 1.0
        })
    )
