import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und MassIndex
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'MassIndex': 1.0
        })
    )
