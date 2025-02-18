import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'ProjectionBands': 1.0
        })
    )
