import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
