import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_AAIISentiment_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und AAIISentiment
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'AAIISentiment': 1.0
        })
    )
