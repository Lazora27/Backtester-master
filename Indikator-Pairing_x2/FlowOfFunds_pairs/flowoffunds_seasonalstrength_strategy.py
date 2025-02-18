import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FlowOfFunds_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FlowOfFunds und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'FlowOfFunds': 1.0,
            'SeasonalStrength': 1.0
        })
    )
