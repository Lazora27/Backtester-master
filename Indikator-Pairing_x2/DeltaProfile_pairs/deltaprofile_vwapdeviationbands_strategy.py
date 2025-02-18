import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
