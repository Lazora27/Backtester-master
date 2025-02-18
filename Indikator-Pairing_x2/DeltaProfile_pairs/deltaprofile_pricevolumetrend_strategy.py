import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
