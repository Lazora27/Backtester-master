import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und CCITurbo
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'CCITurbo': 1.0
        })
    )
