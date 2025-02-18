import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'MACDPredictor': 1.0
        })
    )
