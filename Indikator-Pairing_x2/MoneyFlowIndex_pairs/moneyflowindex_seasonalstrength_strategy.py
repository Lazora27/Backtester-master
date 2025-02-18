import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MoneyFlowIndex_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MoneyFlowIndex und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'MoneyFlowIndex': 1.0,
            'SeasonalStrength': 1.0
        })
    )
