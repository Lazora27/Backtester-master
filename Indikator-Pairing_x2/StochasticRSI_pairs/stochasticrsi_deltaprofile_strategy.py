import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'DeltaProfile': 1.0
        })
    )
