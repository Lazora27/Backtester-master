import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'WolfeWaves': 1.0
        })
    )
