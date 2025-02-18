import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_SharpeRatioIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und SharpeRatioIndicator
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'SharpeRatioIndicator': 1.0
        })
    )
