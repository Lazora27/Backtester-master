import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und CCITurbo
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'CCITurbo': 1.0
        })
    )
