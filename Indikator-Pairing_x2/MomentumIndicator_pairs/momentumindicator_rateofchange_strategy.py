import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und RateOfChange
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'RateOfChange': 1.0
        })
    )
