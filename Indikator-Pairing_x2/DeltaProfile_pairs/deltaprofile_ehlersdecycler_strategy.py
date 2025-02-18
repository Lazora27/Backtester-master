import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'EhlersDecycler': 1.0
        })
    )
