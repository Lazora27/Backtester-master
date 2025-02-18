import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'SeasonalStrength': 1.0
        })
    )
