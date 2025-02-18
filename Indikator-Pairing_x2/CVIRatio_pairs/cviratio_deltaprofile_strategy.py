import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'DeltaProfile': 1.0
        })
    )
