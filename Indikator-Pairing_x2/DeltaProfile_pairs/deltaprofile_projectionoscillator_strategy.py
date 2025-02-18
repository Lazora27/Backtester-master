import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
