import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'BradleySiderograph': 1.0
        })
    )
