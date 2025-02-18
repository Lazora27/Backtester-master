import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
