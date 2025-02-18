import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
