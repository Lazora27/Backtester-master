import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_HyperbolicVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und HyperbolicVolatility
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'HyperbolicVolatility': {
                'class': HyperbolicVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HyperbolicVolatility'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'HyperbolicVolatility': 1.0
        })
    )
